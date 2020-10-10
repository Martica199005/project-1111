Two files are provided with this assignment:
train.txt

test.txt
Each file is a collection of texts, one sentence per line. 
train.txt contains 10,000 sentences from the NewsCrawl corpus. You will use this corpus to train the language models. 

The test corpus test.txt is from the same domain and will be used to evaluate the language models that you trained.

PRE-PROCESSING
Prior to training, please complete the following pre-processing steps:

1)Pad each sentence in the training and test corpora with start and end symbols (you can use <s> and </s>, respectively).

2)Lowercase all words in the training and test corpora. Note that the data already has been tokenized (i.e. the punctuation has been split off words).

3)Replace all words occurring in the training data once with the token <unk>. Every word in the test data not seen in training should be treated as <unk>.


To do:
 -How many word types (unique words) are there in the training corpus? Please include the padding symbols and the unknown token.
 
- How many word tokens are there in the training corpus?


The Python code along with a README file that has instructions on how to run it in order to obtain the answers to questions in Section 1.3
The report that includes the answers to the questions in PART I and PART II in Sec- tion 1.3