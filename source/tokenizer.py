import regex
from normalizer import normalize_text

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
NUMBER_PATTERN = r"\d+(?:\.\d+)?"

EMOJI_PATTERN = (
    r"\p{Extended_Pictographic}"
    r"(?:\uFE0F|\p{Emoji_Modifier})?"
    r"(?:\u200D\p{Extended_Pictographic}"
    r"(?:\uFE0F|\p{Emoji_Modifier})?)*"
)

WORD_PATTERN = r"[\p{L}\p{M}\p{N}_]+(?:['’][\p{L}\p{M}\p{N}_]+)*"

OTHER_PATTERN = r"[^\s]"
TOKEN_PATTERN = (
        DATE_PATTERN
        + "|"
        + NUMBER_PATTERN
        + "|"
        + EMOJI_PATTERN
        + "|"
        + WORD_PATTERN
        + "|"
        + OTHER_PATTERN
)

def tokenize(text):

    text = normalize_text(text)
    tokens = regex.findall(TOKEN_PATTERN, text)
    return tokens
