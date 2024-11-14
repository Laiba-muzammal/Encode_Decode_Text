# Encode-Decode Text Game
<pre> Rules:
1. The user will be asked to input some text.
2. The user can then choose whether to encode or decode the text.
3. Encoding and decoding rules:
     - If the text is 1 character long, it remains unchanged.
     - If the text is 2 characters long, the characters are reversed for encoding and decoding.
     - If the text is longer than 2 characters:
      - For encoding: The first character of the text moves to the end, and 3 random characters are added at the start and end of the encoded text.
      - For decoding: The random characters are stripped, and the last character of the remaining text is moved to the front to restore the original.
4. If the text length is not valid for decoding, it will show an error message.
5. The game allows the user to play multiple rounds until they choose to exit. </pre>
