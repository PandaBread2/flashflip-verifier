# flashflip verifier

This is a tool you can use to verify games played on flashflip, the world's first provably fair Discord casino.

As of today, flashflip is the world's most popular Discord casino with over 1,000 users, a bankroll of over $20,000, and a wagered volume of over $2.5M.

## Important Links

- [flashflip Discord server](https://flashflip.io)
- [flashflip informational website](https://flashcrash.io)

## Significance

In order for an online casino to be provably fair, the operator has to demonstrably verify that they cannot affect the outcomes of the games (regardless of the bet amount), and that the games conform with the advertised house edge. You can learn more about the way flashflip manifests its house edge [here](https://medium.com/@flashflip/the-two-methods-of-house-edge-manifestation-2892da7bbb04). 

flashflip employs a standard client-server seed-based architecture for its provably fair system. Games are generated using:
- a client seed that is chosen by the player 
- an iterative nonce to prevent players from replaying the same games
- a server seed that flashflip keeps secret until the end of the day

Each client seed is by default appended with the user's Discord ID, which is randomized by Discord and cannot be chosen nor influenced by the operator. This is to ensure that no two players can have the same client seed (and thus the same chain of games set to differing nonces). The server seed is released daily, allowing users to verify all of their past bets.

## Usage

Download the `verifier.py` file and run it in your favourite Python environment. 

In the system arguments section, input your game details in the format `game, client seed, first nonce, last nonce, server seed`. This will generate the list of games that are derived from your given client and server seeds between your two given nonces. You can then check to see if the results generated align with the results flashflip gave to you, thus verifying them.
