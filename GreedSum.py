import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def greed_sum(text, num_sent, min_df=1, max_df=1.0):
        
    #fit a TFIDF vectorizer
    vectorizer = TfidfVectorizer(min_df=min_df, max_df=max_df)
    vectorizer.fit(text)
    
    #get the matrix
    X = vectorizer.transform(text).toarray()
    
    #get the sentence indices
    idx = []
    while sum(sum(X)) != 0:
        ind = np.argmax(X.sum(axis=1))
        idx.append(ind)

        #update the matrix deleting the columns corresponding to the words found in previous step
        cols = X[ind]
        col_idx = [i for i in range(len(cols)) if cols[i] > 0]
        X = np.delete(X, col_idx, 1)
        
           
    idx = idx[:num_sent]
    idx.sort()
    
    summary = [text[i] for i in idx]
    return summary
    
def main():
    #parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fname', help="Summarization input file name")
    parser.add_argument('--output_fname', help="Summarization output file name")
    parser.add_argument('--min_df', help="Minimum document frequency word threshold")
    parser.add_argument('--max_df', help="Maximum document frequency word threshold")
    parser.add_argument('--num_sent', help="Number of sentences for summary")
    
    args = parser.parse_args()
    
    if not args.input_fname:
        print("No output file name was provided, quitting")
        quit
    else:
        INPUT_FILENAME = args.input_fname
        print("Input file name was provided:", INPUT_FILENAME)
    
    OUTPUT_FILENAME = 'summary_output.txt' #the default file name
    if not args.output_fname:
        print("No output file name was provided, using the default", OUTPUT_FILENAME)
    else:
        OUTPUT_FILENAME = args.output_fname
        print("Output file name was provided:", OUTPUT_FILENAME)
        
    MIN_DF = 1 #the default min_df   
    if not args.min_df:
        print("No minimum document frequency parameter was provided, using the default", MIN_DF)
    else:
        MIN_DF = float(args.min_df)
        print("Minimum document frequency parameter was provided:", MIN_DF)
        
    MAX_DF = 1 #the default max_df   
    if not args.max_df:
        print("No maximum document frequency parameter was provided, using the default", MAX_DF)
    else:
        MAX_DF = float(args.max_df)
        print("Maximum document frequency parameter was provided:", MAX_DF)
        
    NUM_SENT = 1 #the default max_df   
    if not args.num_sent:
        print("No number of sentences was provided, using the default", NUM_SENT)
    else:
        NUM_SENT = int(args.num_sent)
        print("Number of sentences was provided:", NUM_SENT)
        
        
    # 1. Get the text from the file provided
    f = open(INPUT_FILENAME, 'r')
    text = ' '.join(f.readlines()).replace('\n',' ').replace('  ',' ').split('. ')
    f.close()
    
    # 2. Summarize
    summary = greed_sum(text, NUM_SENT, min_df=MIN_DF, max_df=MAX_DF)

    # 3. Save summary to a file
    f = open(OUTPUT_FILENAME, 'w')
    f.writelines(summary)
    f.close()
    
if __name__ == "__main__":
    main()