"""
Tests for anonymize module.
"""
import pandas as pd
import pytest
from inforcehub import Anonymize


@pytest.fixture(scope="module")
def test_df():
    # Load test data into dataframe - copy this when running tests
    return pd.read_csv("test/test_fixtures/test_product_data.csv")


class TestInforcehubAnon(object):

    anon = Anonymize(salt="PASSWORDTHING")  # This is our test salt

    def test_anon_init_is_random(self):
        """ Test that new anon instances have randomised salt """
        a = Anonymize()
        b = Anonymize()
        text = "Test thing"
        assert a.salt != b.salt
        assert a.encode(text) != b.encode(text)
        assert a.encode(text) != self.anon.encode(text)

    def test_anon_result_with_known_password(self):
        """ Tests the output hex value is as expected when password is set and known """
        assert self.anon.salt == "PASSWORDTHING".encode()
        assert self.anon.encode("This is a thing") == "9ecdcb0b584d922c1d9af10d77edd522"

    def test_encode_produces_string(self):
        """ Tests the output value of the encode routine """
        assert isinstance(self.anon.encode("Something"), str)
        assert len(self.anon.encode("Something else")) == 32

    def test_raises_exception_on_column_error(self, test_df):
        """ Tests that columns that don't exist raises an exception """
        df = test_df.copy()
        with pytest.raises(Exception):
            self.anon.transform(df, ["First name", "Error name"])
        with pytest.raises(Exception):
            self.anon.transform(df, "Single error column name")

    def test_columns_transformed_OK(self, test_df):
        """ Tests that the test dataframe is converted correctly """
        df = test_df.copy(deep=True)
        self.anon.transform(df, "Contract number")
        assert df.shape == test_df.shape
        assert df["Contract number"].iloc[0] == "c5e8b35adac40efce02cc69487b3addc"
        assert test_df["Contract number"].iloc[0] == 33463634
        assert df["Contract number"].all() != test_df["Contract number"].all()
        assert df["Product"].iloc[2] == "Mousetrap Pro"
        assert df["Product"].all() == test_df["Product"].all()

    def test_pseudo_anon_dataset(self, test_df):
        """ Tests that the pseudo_anonymised dataset is valid """
        df = test_df.copy(deep=True)
        key_df = self.anon.transform(df, ["Contract number", "Status"])
        assert key_df.shape[1] == 4
        assert key_df["Contract number_"].iloc[0] == "c5e8b35adac40efce02cc69487b3addc"
        assert key_df["Contract number"].iloc[0] == 33463634
        assert key_df["Status_"].iloc[3] == "e76e1e08dbbe5b255724b6520cbb5497"
        assert key_df["Status"].iloc[3] == "Paid-up"

    def test_multiple_columns_transformed(self, test_df):
        """ Tests that multiple columns are transformed correctly """
        df = test_df.copy(deep=True)
        self.anon.transform(df, ["First name", "Product", "Start date"])
        assert df.shape == test_df.shape
        for column in ["Contract number", "Last name", "Status", "In-force premium"]:
            assert df[column].all() == test_df[column].all()
        for column in ["First name", "Product", "Start date"]:
            assert df[column].all() != test_df[column].all()
            assert isinstance(df[column].iloc[3], str)
            assert len(df[column].iloc[3]) == 32

    def test_same_names_give_same_hash(self, test_df):
        """ Tests that the same text in the input will have the same hash """
        """ Checks that we haven't updated the salt by accident """
        df = test_df.copy(deep=True)
        self.anon.transform(df, ["Last name", "Product"])
        # Both surnames are Brown
        assert len(df["Last name"].iloc[3]) == 32
        assert df["Last name"].iloc[3] == df["Last name"].iloc[4]
        # Same product names for first and second row
        assert df["Product"].iloc[0] == df["Product"].iloc[1]
        assert df["Product"].iloc[0] != df["Product"].iloc[3]
