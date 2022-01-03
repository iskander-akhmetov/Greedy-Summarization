# Greedy-Summarization
Here you will find the source codes for the paper "Greedy Optimization Method for Extractive Summarization of Scientific Articles" which you can find at https://ieeexplore.ieee.org/document/9654190.

Abstract:
This work presents a method for summarizing scientific articles from the arXive and PubMed datasets using a greedy Extractive Summarization algorithm. We used the approach along with Variable Neighborhood Search (VNS) to learn what is the top-line exists in the area of Extractive Text Summarization quality in terms of ROUGE scores. The algorithm is based on first selecting for the summary the sentences from the text containing the maximum number of words with the higher TFIDF values along with minimum document frequency parameter tuning for TFIDF vectorization. As a result, the method achieves 0.43/0.12 and 0.40/0.13 for ROUGE-1/ROUGE-2 scores on arXive and PubMed datasets, respectively. These results are comparable to the state-of-the-art models using complex neural network architectures and serious computational resources together with the large amounts of training data. In contrast, our method uses a straightforward statistical inference methodology.

Please cite it as:

I. Akhmetov, A. Gelbukh and R. Mussabayev, "Greedy Optimization Method for Extractive Summarization of Scientific Articles," in IEEE Access, vol. 9, pp. 168141-168153, 2021, doi: 10.1109/ACCESS.2021.3136302.

OR

@ARTICLE{9654190,
  author={Akhmetov, Iskander and Gelbukh, Alexander and Mussabayev, Rustam},
  journal={IEEE Access}, 
  title={Greedy Optimization Method for Extractive Summarization of Scientific Articles}, 
  year={2021},
  volume={9},
  number={},
  pages={168141-168153},
  doi={10.1109/ACCESS.2021.3136302}}

# Instructions
Run GreedSum.py with the following parameters:

--input_fname the name of a file with the scientific article text you need to summarize.

--output_fname the name of a file where you want to put your summary, default is summary_output.txt.

--min_df minimum document frequency parameter, default is 1.0, but use something around 0.03 for best results.

--max_df maximum document frequency parameter, does not really affect anything, but just in case try playing with it may be in your case it will matter, the default is 1.0.

--num_sent defines how many sentences you want to extract from the source text for your summary, default is 1.

Example: python GreedSum.py --input_fname=sample_article.txt --num_sent=10
