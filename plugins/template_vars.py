from datasette import hookimpl
from bs4 import BeautifulSoup as Soup
import html
import re

non_alphanumeric = re.compile(r"[^a-zA-Z0-9\s]")
multi_spaces = re.compile(r"\s+")


def first_paragraph(html):
    soup = Soup(html, "html.parser")
    return str(soup.find("p"))


def noteURLPath(note):
    return f"/pages/{note['topic']}-{note['slug']}-{note['id']}"


def highlight(s):
    s = html.escape(s)
    s = s.replace("b4de2a49c8", "<strong>").replace("8c94a2ed4b", "</strong>")
    return s


@hookimpl
def extra_template_vars(request, datasette):
    async def related_tils(note):
        text = note["title"] + " " + note["body"]
        text = non_alphanumeric.sub(" ", text)
        text = multi_spaces.sub(" ", text)
        words = list(set(text.lower().strip().split()))
        sql = """
        select
          note.id, note.topic, note.slug, note.title, note.created
        from
          note
          join note_fts on note.rowid = note_fts.rowid
        where
          note_fts match :words
          and not (
            note.slug = :slug
            and note.topic = :topic
          )
        order by
          note_fts.rank
        limit
          5
        """
        result = await datasette.get_database().execute(
            sql,
            {"words": " OR ".join(words), "slug": note["slug"], "topic": note["topic"]},
        )
        return result.rows

    return {
        "q": request.args.get("q", ""),
        "highlight": highlight,
        "first_paragraph": first_paragraph,
        "related_tils": related_tils,
        "noteURLPath": noteURLPath,
    }


@hookimpl
def prepare_connection(conn):
    conn.create_function("first_paragraph", 1, first_paragraph)
