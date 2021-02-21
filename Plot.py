import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from Create_DataFrame import probability_dataframe

# graphing_data = pd.DataFrame({'Box 1': probability_box1[:, 0],
#                               'Box 2': probability_box2[:, 0],
#                               'Box 3': probability_box3[:, 0],
#                               'First Coin: Gold': probability_firstcoin_gold[:, 0],
#                               'First Coin: Silver': probability_firstcoin_silver[:, 0],
#                               'Second Coin: Gold': probability_secondcoin_gold[:, 0],
#                               'Second Coin: Silver': probability_secondcoin_silver[:, 0],
#                               'Gold': probability_paradox_gold[:, 0],
#                               'Silver': probability_paradox_silver[:, 0]})

initial_df = probability_dataframe(10)
fig, axes = plt.subplots(nrows=2, ncols=3)


axes[0, 0].set_xticks([])
axes[0, 0].set_yticks([])
arr_BBP = mpimg.imread('Bertrand_Box_Paradox.jpg')
imagebox = OffsetImage(arr_BBP, zoom=0.3)
ab = AnnotationBbox(imagebox, (0.5, 0.5))
axes[0, 0].add_artist(ab)
axes[0, 0].axis("off")
plt.grid()
plt.draw()

plt.savefig('add_picture_matplotlib_figure.png', bbox_inches='tight')
initial_df[["Box 1", "Box 2", "Box 3"]].iloc[9, :].plot(ax=axes[1, 0], kind='bar', rot=0)
initial_df[["First Coin: Gold", "First Coin: Silver"]].iloc[9, :].plot(ax=axes[0, 1], kind='bar', rot=0)
initial_df[["Second Coin: Gold", "Second Coin: Silver"]].iloc[9, :].plot(ax=axes[1, 1], kind='bar', rot=0)
initial_df[["Gold"]].plot(ax=axes[0, 2], kind='line', rot=0)
initial_df[["Silver"]].plot(ax=axes[1, 2], kind='line', rot=0)

axes[0, 2].set_title('Probability that the second coin\n'
                     'is the same as the first')


def submit(iterations):

    updated_df = probability_dataframe(int(eval(iterations)))

    for k in range(1, int(eval(iterations))):

        axes[1, 0].clear()
        axes[0, 1].clear()
        axes[1, 1].clear()
        axes[0, 2].clear()
        axes[1, 2].clear()

        updated_df[["Box 1", "Box 2", "Box 3"]].iloc[k, :].plot(ax=axes[1, 0], kind='bar', rot=0)
        updated_df[["Second Coin: Gold", "Second Coin: Silver"]].iloc[k, :].plot(ax=axes[1, 1], kind='bar', rot=0)
        updated_df[["First Coin: Gold", "First Coin: Silver"]].iloc[k, :].plot(ax=axes[0, 1], kind='bar', rot=0)

        updated_df[["Gold"]].iloc[0:k, :].plot(ax=axes[0, 2], kind='line', rot=0)
        updated_df[["Silver"]].iloc[0:k, :].plot(ax=axes[1, 2], kind='line', rot=0)

        axes[0, 2].set_title('Probability that the second coin\n'
                             'is the same as the first')

        plt.pause(0.001)


axbox = plt.axes([0.5, 0.001, 0.075, 0.065])
text_box = TextBox(axbox, 'Iterations (1 to 1000)', initial="10", label_pad=0.25)
text_box.on_submit(submit)

plt.show()
