from typing import List

import pandas as pd


def get_genre_rank(recs: pd.DataFrame, items: dict, user_genres: dict) -> List[int]:
    """
    The function of ranking the recommendations of the model, taking into account the user's favorite genres.
    recos: dataframe with model recommendations;
    items: dictionary with movie descriptions;
    user_genres: dictionary with genre weights;
    n: number of recommendations for the user.
    """

    recs = recs[["user_id", "item_id"]]
    items_df = pd.DataFrame(
        {"item_id": recs.item_id, "genres": [items[i] for i in recs.item_id.values]}
    )
    recs = recs.merge(items_df, on="item_id", how="left")
    recs = recs.explode("genres")
    weights_genre = user_genres[recs.user_id[0]]
    recs = recs.merge(
        pd.DataFrame(
            {"genres": weights_genre.keys(), "weight_genre": weights_genre.values()}
        ),
        on=["genres"],
        how="left",
    )
    recs = recs.fillna(0)
    recs = recs.groupby(["user_id", "item_id"]).mean(numeric_only=True)
    recs = recs.sort_values(["weight_genre"], ascending=False)
    recs = recs.reset_index()

    return recs.item_id.to_list()
