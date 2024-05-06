from behave import register_type
import parse

from entities.image import Image
from entities.vote import Vote


# class Vote(object)
#     """
#     """


@parse.with_pattern(r"[^\"].+")
def parse_vote(text):
    return Vote(sub_id=text)


@parse.with_pattern(r"[^\"].+")
def parse_image(text):
    return Image(image_name=text)


register_type(Vote=parse_vote)
register_type(Image=parse_image)
