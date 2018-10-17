.. _anonymizer:

==========
Anonymizer
==========

This module provides methods to **anonymize or pseudo-anonymize a dataset**.

**Anonymizing** the dataset means removing all the confidential data and 
**not retaining any key** to enable it to be reconstructed. Also the 
remaining patterns in the data should not enable the identity of 
individuals to be identified via other means.

Pseudo-anonymizing the dataset also removes all the confidential
data from the dataset. But we also retain a key or separate
dataset enabling us to decode the original entities if required
at some point in the future.

The anonymizer does not delete the confidential data. Instead it 
**one-way encrypts (hashes) the data** so that the original text or
numbers cannot be retrieved. 

Encryption is better than deletion because the pattern of data is 
useful information we want our models to be able to use. For example 
it may be that one customer has multiple contracts. Deleting the 
customer number loses the information that these contracts are linked
but encryption retains those relationships.


Encryption method
=================

The method used is similar to password hashing.

*   A **salt** is randomly created for this encryption
    run by the system. If desired for reproducability, the
    user can override the salt with a passphrase of their 
    choice.

*   The salt is prepended to each value to be encrypted

*   The encryption algorithm converts the salted value into
    a long hexidecimal hash. This is our encrypted value.

Encryption is done using the **python hashlib package**. 
Using the **md5 algorithm**. More details can be found at  
https://docs.python.org/3/library/hashlib.html

The randomized salt is created using the **bcrypt package**.
More details can be found at https://pypi.org/project/bcrypt/

.. note::

    In a password setting, usually for each 
    individual encryption, a new random salt value
    would be created. This way you get very strong encryption
    with a key (the salt) that changes for every password.
    
    However in our algorithm we only set the salt once for the 
    full dataset. This is on purpose so that we can retain the 
    relationship structure between values whilst still providing 
    a good level of encryption by using a hash algorithm and 
    a salt value. 
    
    What this means is that the same customer
    occuring in multiple rows will have the same hashed value
    using our method.  



Usage
=====

Import the anonymizer class::

    from inforcehub import Anonymize
    
On initializing, the object will use a new randomized salt passphrase::

    anon = Anonymize()

You need to decide which columns in your Pandas dataframe
should be anonymized.

To transform a dataframe use the **transform** method on the anon
object.
We pass in the dataframe to be transformed, and a list of the 
columns to be anonymized::

    anon.transform(df, ['columnA', 'colummZ'])

The dataframe **df** itself will be anonymized to save improve 
memory usage and speed for large datasets. To
retain a copy of the original make a deep copy of the dataframe
before transforming it::

    original_df = df.copy(deep=True)  # Do this first

If **pseudo-anonymization** is required instead of full anonymization
the **lookup** dataframe of encrypted and unencrypted values is 
returned. This can be used later as a lookup to return to the 
confidential data::

    lookup_df = anon.transform(df, ['columnA', 'colummZ'])


Module details
==============

.. automodule:: inforcehub.anonymize
   	:members: