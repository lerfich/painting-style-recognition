from typing import List

import cv2
import numpy as np
from domain.classifiers.base_classifier import BaseClassifier


class FREAKClassifier(BaseClassifier):

    def get_features(self, image: np.ndarray) -> List:
        fast = cv2.FastFeatureDetector_create()
        kp = fast.detect(image,None)

        freakExtractor = cv2.xfeatures2d.FREAK_create()
        kp,descriptors= freakExtractor.compute(image,kp)

        desc = cv2.resize(descriptors, (250, 250))
        desc = desc.reshape(250, 250)

        return desc
