# Hans Kamin
# Spring 2017

# Function to create and train a Markov Chain with all of
# Logic's lyrics.

def train_markov_chain(lyrics):
    """
    Args:
      - lyrics: a list of strings, where each string represents
                the lyrics of one song by an artist.
    
    Returns:
      A dict that maps a tuple of 2 words ("bigram") to a list of
      words that follow that bigram, representing the Markov
      chain trained on the lyrics.
    """
    
    # Initialize the beginning of our chain.
    chain = {
        (None, "<START>"): []
    }
    
    for lyric in lyrics:
        # Replace newline characters with our tag.
        lyric_newlines = lyric.replace('\n', ' <N> ')
        # Create a tuple representing the current bigram.
        last_2 = (None, "<START>")
        for word in lyric_newlines.split():
            # Add the word as one that follows the current bigram.
            chain[last_2].append(word)
            # Shift current bigram to account for newly added word.
            last_2 = (last_2[1], word)
            if last_2 not in chain:
                chain[last_2] = []
        chain[last_2].append("<END>")
    
    return chain

# Load the lyrics object we stored earlier.
import pickle
lyrics = pickle.load(open("lyrics.pkl", "rb"))

# Train a Markov Chain over all of Logic's lyrics.
chain = train_markov_chain(lyrics)
