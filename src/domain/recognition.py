from collections import Counter
from typing import List, Tuple

from domain.classifiers import HCDClassifier, FREAKClassifier, HoGClassifier
from domain.utils.load_data import load
from domain.utils.plots import plot_hcd, plot_hog, plot_freak


def recognition(image: List) -> Tuple[str, List]:
    """Классификация стиля изображения.

    Args:
        image (List):
            входные изображения.

    Returns:
        Tuple[str, List]:
            метки классов,
            результаты работы дескрипторов.
    """
    # load train sample
    data = load()

    # create classifiers for voting classification 
    classifiers = [
        HoGClassifier(),
        FREAKClassifier(),
        HCDClassifier()
    ]

    # split data to X and y
    X_train = [img for img, _ in data]
    y_train = [style for _, style in data]

    # fit classifiers
    for classifier in classifiers:
        classifier.fit(X_train, y_train)

    # predict
    class_marks = Counter()
    features = []
    results = []
    for classifier in classifiers:
        mark_with_feature = classifier.predict(image)
        class_marks[mark_with_feature[0][0]] += 1
        results.append(mark_with_feature[0][0])
        features.append(mark_with_feature[0][1])

    # retrieve most common mark
    mark = class_marks.most_common(1)[0][0]
    print(results, 'results')

    descriptors = [
        plot_hog(features[0]),
        plot_hcd(features[1]),
        plot_freak(features[2])
    ]

    return mark, results, descriptors
