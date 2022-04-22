example = open ('contracts/ExampleNFT.cdc', 'rt')
fighter = open('contracts/UFC_FIGHTER_NFT.cdc', 'wt')
for line in example:
	fighter.write(line.replace('ExampleNFT', 'UFC_FIGHTER_NFT').replace('exampleNFT', 'UFC_FIGHTER_NFT'))
example.close()
fighter.close()
