from enum_definitions import Codemian_Style, Topic
from joke_bot import Bot

test_bot = Bot(
    rating_model=None,
    style=Codemian_Style.KEVIN_HART,
    topic=Topic.POLITICS,
    name="b"
)


print(test_bot.get_prompt)
print(test_bot.tell_joke(topic=Topic.RELIGION))
