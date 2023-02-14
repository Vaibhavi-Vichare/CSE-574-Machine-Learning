import sys
import simpledorff
import pandas as pd

if __name__ == '__main__':
    fname = sys.argv[1]
    Data = pd.read_csv(fname)  # Load Your Dataframe
    new_df = pd.DataFrame(columns=['tweet_id', 'annotator_id', 'annotation'])
    for i in range(0, Data.shape[0]):
        t_id = Data.iloc[i]['tweet_id']
        for j in range(0, 3):
            l = [t_id, j + 1, Data.iloc[i]['annotator_' + str(j + 1)]]
            new_df = new_df.append(pd.DataFrame(data=[l], columns=['tweet_id', 'annotator_id', 'annotation']),
                                   ignore_index=True)
    alpha = simpledorff.calculate_krippendorffs_alpha_for_df(new_df, experiment_col='tweet_id',
                                                     annotator_col='annotator_id',
                                                     class_col='annotation')
    a1_a2_agreement = Data[Data['annotator_1'] == Data['annotator_2']].shape[0] / 50
    a1_a3_agreement = Data[Data['annotator_1'] == Data['annotator_3']].shape[0] / 50
    a2_a3_agreement = Data[Data['annotator_2'] == Data['annotator_3']].shape[0] / 50
    avg_agreement = (a1_a2_agreement + a2_a3_agreement + a1_a3_agreement) / 3

    print(str(alpha) + '\t' + str(avg_agreement))
