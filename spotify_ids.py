"""file = []
inputText = ''
splits = ''
for i in range(1, 21):
    file.append(open('C:/Users/Bharat Bojja/Documents/Programming/SongClassification/PlayLists/PlayList' + str(i) + '.txt', 'r', encoding='utf-8'));
    inputText += file[i - 1].read()"""

file = open('C:/Users/Bharat Bojja/Documents/Programming/SongClassification/PlayLists/PlayList11.txt', 'r', encoding='utf-8')
inputText = file.read()

splits = inputText.split("spotify:track:")

for str in splits:
    print(str[:22])

print(len(splits))