from enum import Enum
from typing import List, Optional, TypedDict, Union, Callable

from simsapa import ShowLabels
from simsapa.app.db import appdata_models as Am
from simsapa.app.db import userdata_models as Um
from simsapa.app.search.helpers import SearchResult

USutta = Union[Am.Sutta, Um.Sutta]
UDictWord = Union[Am.DictWord, Um.DictWord]
ULink = Union[Am.Link, Um.Link]

UDeck = Union[Am.Deck, Um.Deck]
UMemo = Union[Am.Memo, Um.Memo]

UBookmark = Union[Am.Bookmark, Um.Bookmark]
UDocument = Union[Am.Document, Um.Document]

UChallengeCourse = Union[Am.ChallengeCourse, Um.ChallengeCourse]
UChallengeGroup = Union[Am.ChallengeGroup, Um.ChallengeGroup]
UChallenge = Union[Am.Challenge, Um.Challenge]

UMultiRef = Union[Am.MultiRef, Um.MultiRef]

class Labels(TypedDict):
    appdata: List[str]
    userdata: List[str]

class SearchArea(int, Enum):
    Suttas = 0
    DictWords = 1

class SearchMode(int, Enum):
    FulltextMatch = 0
    ExactMatch = 1
    HeadwordMatch = 2
    TitleMatch = 3

AllSearchModeNameToType = {
    "Fulltext Match": SearchMode.FulltextMatch,
    # FIXME disabled ExactMatch while its buggy.
    # "Exact Match": SearchMode.ExactMatch,
    "Headword Match": SearchMode.HeadwordMatch,
    "Title Match": SearchMode.TitleMatch,
}

SuttaSearchModeNameToType = {
    "Fulltext Match": SearchMode.FulltextMatch,
    # "Exact Match": SearchMode.ExactMatch,
    "Title Match": SearchMode.TitleMatch,
}

DictionarySearchModeNameToType = {
    "Fulltext Match": SearchMode.FulltextMatch,
    # "Exact Match": SearchMode.ExactMatch,
    "Headword Match": SearchMode.HeadwordMatch,
}

class SearchParams(TypedDict):
    mode: SearchMode
    page_len: Optional[int]
    lang: Optional[str]
    lang_include: bool
    source: Optional[str]
    source_include: bool
    enable_regex: bool
    fuzzy_distance: int

class QueryType(str, Enum):
    suttas = "suttas"
    words = "words"

class SuttaQueriesInterface:
    get_sutta_by_url: Callable

class DictionaryQueriesInterface:
    get_words_by_uid: Callable
    words_to_html_page: Callable
    render_html_page: Callable
    get_word_html: Callable
    dict_word_from_result: Callable[[SearchResult], Optional[UDictWord]]

class QuoteScope(str, Enum):
    Sutta = 'sutta'
    Nikaya = 'nikaya'
    All = 'all'

QuoteScopeValues = {
    'sutta': QuoteScope.Sutta,
    'nikaya': QuoteScope.Nikaya,
    'all': QuoteScope.All,
}

class SuttaQuote(TypedDict):
    quote: str
    selection_range: Optional[str]

class GraphRequest(TypedDict):
    sutta_uid: Optional[str]
    dict_word_uid: Optional[str]
    distance: int
    queue_id: str
    graph_gen_timestamp: float
    graph_path: str
    messages_url: str
    labels: Optional[ShowLabels]
    min_links: Optional[int]
    width: int
    height: int
