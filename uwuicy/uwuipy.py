import re
import random as rand


class uwuipy:
    
    __uwu_pattern = []

    __actions = [
        '*blushes*',
        '*whispers to self*',
        '*cries*',
        '*screams*',
        '*sweats*',
        '*dances*',
        '*runs away*',
        '*laughs*',
        '*walks away*',
        '*looks at you*',
        '*starts dancing*',
        '*huggles tightly*',
        '*boops your nose*',
        '*wags tail*',
        '*pounces on you*',
        '*nuzzles your necky wecky*',
        '*licks lips*',
        '*jumps and huggles*',
        '*jumps*',
        '*looks around suspiciously*',
        '*laughs smuggly*',
        '*breaks into your house*',
        '*smiles*',
        '*UwU*',
	'*dies*',
	'*growls*',
	'*fights*'
    ]

    __faces = [
        "(・\`ω\´・)",
        ";;w;;",
        "OwO",
        "owo",
        "UwU",
        "\>w\<",
        "^w^",
        "ÚwÚ",
        "^-^",
        ":3",
        "x3",
        'Uwu',
        'uwU',
        '(uwu)',
        "(ᵘʷᵘ)",
        "(ᵘﻌᵘ)",
        "(◡ ω ◡)",
        "(◡ ꒳ ◡)",
        "(◡ w ◡)",
        "(◡ ሠ ◡)",
        "(˘ω˘)",
        "(⑅˘꒳˘)",
        "(˘ᵕ˘)",
        "(˘ሠ˘)",
        "(˘³˘)",
        "(˘ε˘)",
        "(˘˘˘)",
        "( ᴜ ω ᴜ )",
        "(„ᵕᴗᵕ„)",
        "(ㅅꈍ ˘ ꈍ)",
        "(⑅˘꒳˘)",
        "( ｡ᵘ ᵕ ᵘ ｡)",
        "( ᵘ ꒳ ᵘ ✼)",
        "( ˘ᴗ˘ )",
        "(ᵕᴗ ᵕ⁎)",
        "*:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:*",
        "*˚*(ꈍ ω ꈍ).₊̣̇.",
        "(。U ω U。)",
        "(U ᵕ U❁)",
        "(U ﹏ U)",
        "(◦ᵕ ˘ ᵕ◦)",
        "ღ(U꒳Uღ)",
        "♥(。U ω U。)",
        "– ̗̀ (ᵕ꒳ᵕ) ̖́-",
        "( ͡U ω ͡U )",
        "( ͡o ᵕ ͡o )",
        "( ͡o ꒳ ͡o )",
        "( ˊ.ᴗˋ )",
        "(ᴜ‿ᴜ✿)",
        "~(˘▾˘~)",
        "(｡ᴜ‿‿ᴜ｡)",
    ]

    def __init__(self, seed: int = None, face_chance: float = 0.05, action_chance: float = 0.075):

        # input protection to make sure the user stays within allowed parameters
        if not 0.0 <= face_chance <= 1.0:
            raise ValueError("Invalid input value for faceChance, supported range is 0-1.0")
        elif not 0.0 <= action_chance <= 1.0:
            raise ValueError("Invalid input value for actionChance, supported range is 0-1.0")

        rand.seed(seed)
        self._face_chance = face_chance
        self._action_chance = action_chance

    def _uwuify_words(self, _msg):
        # split the message into words
        words = _msg.split(' ')
        
        # iterate over each individual word
        # sure you could regex the entire thing, but then you lose
        # the ability to ignore certain cases, like pings and urls
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip URLs
            if re.search(r'((http:|https:)//[^ \<]*[^ \<\.])', word):
                continue
            # skip pings
            if word[0] == '@' or word[0] == '#' or word[0] == ':' or word[0] == '<':
                continue
            # for each pattern in the array
            for pattern, substitution in self.__uwu_pattern:
                # attempt to use the pattern on the word
                word = re.sub(pattern, substitution, word)
            
            # add the modified word to the original words array
            words[idx] = word

        # return the joined string
        return ' '.join(words)

    def _uwuify_spaces(self, _msg):
        # split the message into words
        words = _msg.split(' ')

        # iterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip pings
            if word[0] == '@' or word[0] == '#' or word[0] == ':' or word[0] == '<':
                continue
            
            # get the character case for the second letter in the word
            next_char_case = word[1].isupper() if len(word) > 1 else False
            _word = ''
            
            # if we are to add a face, do it
            if rand.random() <= self._face_chance:
                _word = (_word or word) + ' ' + self.__faces[rand.randrange(0, len(self.__faces))]
                
            # if we are to add an action, do it
            if rand.random() <= self._action_chance:
                _word = (_word or word) + ' ' + self.__actions[rand.randrange(0, len(self.__actions))]
                
            # replace the word in the array with the modified if it exists, if not add the original word back
            words[idx] = (_word or word)

        return ' '.join(words)
            
    def uwuify(self, msg):
        msg = self._uwuify_words(msg)
        msg = self._uwuify_spaces(msg)

        return msg
