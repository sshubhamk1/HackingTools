## Generation of prime number p,q from n

` Use factordb website`

## Command to decrypt the cipher.dat file

`openssl rsautl -decrypt -inkey private_key.pem -in cipher.dat -out decrypted_message.txt`

## Command to encrypt the plain.txt

`openssl rsautl -encrypt -inkey public_key.pem -pubin -in decrypted_message.txt -out ciphertext.enc`