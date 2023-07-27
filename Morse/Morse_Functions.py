# decoder
def decode(S):
    # Dictionary from morse to english
    DecodeDict = {'._': 'A', '_...': 'B', '._._': 'C', '_..': 'D', '.': 'E', '.._.': 'F', '__.': 'G', '....': 'H',
                  '..': 'I', '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O', '.__.': 'P', '__._': 'Q'
        , '._.': 'R', '...': 'S', '_': 'T', '.._': 'U', '..._': 'V', '___.': 'W', '_.._': 'X'
        , '_.__': 'Y', '__..': 'Z', '_____': '0', '.____': '1', '..___': '2', '...__': '3', '...._': '4',
                  '.....': '5', '____.': '6', '___..': '7', '__...': '8', '_....': '9', '/': ' '}

    eng = ''

    # traversing and substituting via a loop

    S = S.split()
    for i in S:
        temp = DecodeDict[i]
        eng = eng + temp
    return eng


def encode(S):
    # Dictionary from english to morse
    encodeDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
                  'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
                  '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                  ' ': '/'}

    morse = ''

    # traversing and substituting via a loop
    S = S.upper()
    S = S.split()
    for i in S:
        for j in i:
            temp = encodeDict[j]
            morse = morse + temp + ' '
    return morse
