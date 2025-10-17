import random

first = ["거지", "걸레", "게이", "고자", "고아", "김치", "씹덕", "남창", "냄비", "농아", "돼지", "등신", "따까리", "떨거지", "딸피", "쓰레기", "루저", "맘충", "매국노", "머저리", "멧돼지", "무뇌아", "벌레", "변태", "병신", "븅딱", "빡추", "씹덕", "씨발", "씹", "씹쓰레기", "아다", "엠창", "장애인", "정신병자", "짱깨", "쩌리", "쪼다", "쫄보", "찐따", "호로"]
second = ["년아", "새끼야"]

def retarded(text, func):
    length = len(text)
    if length < 2:
        return text

    position = random.sample(range(length), 2)
    result = list(text)

    for pos in position:
        char = result[pos]
        new = func(char)
        if isinstance(new, list):
            new = ''.join(new)
        result[pos] = new

    return ''.join(result)

# From https://github.com/Mineru98/py-hangul-utils (MIT License) by @Mineru98

CHO_HANGUL = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

CHO_PERIOD = ord("까") - ord("가")
HANGUL_START_CHARCODE = ord("가")

JONG_COMPLETE_HANGUL = {
    "ㄳ": "ㄱㅅ",
    "ㄵ": "ㄴㅈ",
    "ㄶ": "ㄴㅎ",
    "ㄺ": "ㄹㄱ",
    "ㄻ": "ㄹㅁ",
    "ㄼ": "ㄹㅂ",
    "ㄽ": "ㄹㅅ",
    "ㄾ": "ㄹㅌ",
    "ㄿ": "ㄹㅍ",
    "ㅀ": "ㄹㅎ",
    "ㅄ": "ㅂㅅ",
}

JONG_HANGUL = [
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

JONG_PERIOD = ord("개") - ord("가")

JUNG_COMPLETE_HANGUL = {
    "ㅘ": "ㅗㅏ",
    "ㅙ": "ㅗㅐ",
    "ㅚ": "ㅗㅣ",
    "ㅝ": "ㅜㅓ",
    "ㅞ": "ㅜㅔ",
    "ㅟ": "ㅜㅣ",
    "ㅢ": "ㅡㅣ",
}

JUNG_HANGUL = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]

HANGUL_END_CHARCODE = ord("힣")

def divide(word):
    wordCode = ord(word[0])
    charCode = wordCode - HANGUL_START_CHARCODE

    temp = lambda hangul: HANGUL_START_CHARCODE <= hangul <= HANGUL_END_CHARCODE

    if not temp(wordCode):
        return [word[0]]

    choIndex = charCode // CHO_PERIOD
    jungIndex = (charCode % CHO_PERIOD) // JONG_PERIOD
    jongIndex = charCode % JONG_PERIOD

    cho = CHO_HANGUL[choIndex] if choIndex < len(CHO_HANGUL) else ""
    jung = JUNG_HANGUL[jungIndex] if jungIndex < len(JUNG_HANGUL) else ""
    jong = JONG_HANGUL[jongIndex] if jongIndex < len(JONG_HANGUL) else ""

    return cho + jung + jong

def divideHangul(word):
    divided = []
    for char in str(word):
        result = divide(char)
        divided.extend(list(result))
    return divided