#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    print "clean dta"

    from sklearn.linear_model import LinearRegression

    scores = []
    unclean_data = []

    for index, age in enumerate(ages):
        nw = net_worths[index]
        nw_train_copy = list(net_worths)
        ages_train_copy = list(ages)
        pred_copy = list(predictions)

        del ages_train_copy[index]
        del nw_train_copy[index]
        del pred_copy[index]

        reg2 = LinearRegression()
        reg2.fit(nw_train_copy, ages_train_copy)
        score = reg2.score(nw_train_copy, ages_train_copy)
        scores.append(score)
        unclean_data.append((age, nw, score))

    unclean_data.sort(key=lambda x: x[2])

    print "scores", unclean_data
    print "predictions", predictions

    return unclean_data[:80]
