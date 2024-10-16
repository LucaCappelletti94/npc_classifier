"""Submodule to test the execution of the NP Classifier."""

from hammer import Classifier


def test_classifier():
    """Test the NP Classifier."""

    # Initialize the NP Classifier
    classifier = Classifier.load("v1")

    # "O=C1c3c(O/C(=C1/O)c2ccc(O)c(O)c2)cc(O)cc3O" # Quercetin
    # smiles = "CN1[C@H]2CC[C@@H]1[C@@H](C(OC)=O)[C@@H](OC(C3=CC=CC=C3)=O)C2" # Cocaine

    smiles = "O=C1c3c(O/C(=C1/O)c2ccc(O)c(O)c2)cc(O)cc3O"  # Quercetin
    # Classify the molecule
    classification = classifier.predict_proba([smiles])

    print(classification)
