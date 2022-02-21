import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1
train_data = pd.read_csv('train.csv')
train_data.head()

plot_train_data = train_data.set_index('pos')

plot_train_data.loc[:,'A_fraction':'C_fraction'].plot.bar(figsize=(16, 9), stacked=True)
plt.xlabel('Position')
plt.ylabel('Nucleotide frequency')
plt.show()

# 2
mean_matches = train_data['matches'].mean()
train_part = train_data.query('matches > @mean_matches').loc[:, ['pos', 'reads_all', 'mismatches',
                                                                 'deletions', 'insertions']]
train_part.to_csv('train_part.csv')

# 3
mc_donalds_data = pd.read_csv('mc_donalds_data.csv')
mc_donalds_data.head()

mc_donalds_data.describe()

mc_donalds_data.info()

correlate = mc_donalds_data.corr()
plt.figure(figsize=(11, 8))
sns.heatmap(correlate, cmap='RdYlBu', annot=True)

mc_data_ints = mc_donalds_data.iloc[:, 3:]
plt.figure(figsize=(13, 13))
for i in range(mc_data_ints.shape[1]):
    plt.subplot(7, 2, i+1)
    plt.tight_layout()
    plt.hist(x=mc_data_ints.iloc[:, [i]])
    plt.title(mc_data_ints.columns[i])
plt.show()

category_calories = mc_donalds_data.groupby('Category').agg({'Calories': 'mean'}).rename(
    columns={'Calories': 'mean Calories'})
category_calories.sort_values(['mean Calories'])

mc_donalds_data['Category'].value_counts()

# 4
# 4.1


def read_gff(path, names=None):
    gff = pd.read_csv(path, sep='\t', comment='#', header=None, names=names)
    return gff


def read_bed(path, names=None):
    bed = pd.read_csv(path, sep='\t', names=names)
    return bed


gff_df = read_gff('rrna_annotation.gff')
gff_df.head()

# 4.2
gff_df.iloc[:, -1] = gff_df.iloc[:, -1].str.extract('([0-9]+S)')
gff_df.head()

# 4.3
rrna_types = pd.crosstab(gff_df.iloc[:, 0], gff_df.iloc[:, -1])

rrna_types.plot.bar(figsize=(16, 9))
plt.legend(title='RNA type')
plt.xlabel('Sequence')
plt.ylabel('Count')
plt.show()
