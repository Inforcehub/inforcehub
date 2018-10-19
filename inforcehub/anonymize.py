import hashlib
import bcrypt
import pandas as pd


class Anonymize:
    """
    A class that will transform a Pandas dataframe into an anonymized
    dataframe using the python hmac package for encryption.

    When instantiating an object of this class, the **salt**
    init attribute can be specified which enables encryption results
    to be reproduced. If none is supplied, a randomized password
    is created instead for security.

    :param: str salt: an optional passphase - if empty, salt will be randomized
    """

    def __init__(self, salt=None):
        """"""
        if salt:
            # Convert to bytestring
            self.salt = str(salt).encode()
        else:
            self.salt = bcrypt.gensalt()

    def encode(self, text):
        """
        Provides the encryption of a single number, text or date

        :param: text: the text, value or date to be encrypted

        :returns: the hexidecimal encrypted value
        :rtype: str
        """
        return hashlib.md5(self.salt + str(text).encode()).hexdigest()

    def transform(self, df, columns, verbose=False):
        """
        Encrypts the selected columns in a dataframe and returns
        an anonymized dataframe.

        If required, also returns a dataframe of column pairs showing
        the encrypted and original data to be used as a
        pseudo-anonymization key.

        :param: pd.DataFrame() df: A Pandas dataframe to be transformed
        :param: list columns: A list of columns to be transformed
        :param: str verbose: (default=False) If true will print status

        :returns: a pseudo-anonymization lookup table
        :rtype: pd.DataFrame()
        """
        # In case user puts in single column name as a string not a list
        if isinstance(columns, str):
            columns = [columns]

        if verbose:
            print("Will convert columns: %s" % ", ".join(columns))
            print("Encrypting %i rows per column ...\n" % df.shape[0])

        lookup = pd.DataFrame()
        for column in columns:

            if column not in df.columns:
                raise Exception("Column %s cannot be found in dataframe" % column)

            lookup[column] = df[column]

            df[column] = df[column].map(lambda x: self.encode(x))

            lookup[column + "_"] = df[column]

            if verbose:
                print("Finished encrypting column %s" % column)

        return lookup
