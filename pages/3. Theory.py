import streamlit as st

st.header("Theory")
st.markdown("---")

st.markdown("""
### Theory Behind the Attack
RSA key generation involves these steps:
1.  Choose two distinct, small prime numbers, `p` and `q`.
2.  Calculate the value of n : `n = p * q`.
3.  Calculate phi function: `φ(n) = (p-1) * (q-1)`.
4.  Choose a public exponent `e` that is coprime to `φ(n)`.
5.  Calculate the private exponent `d` such that `d * e ≡ 1 (mod φ(n))`.

The **public key** is `(e, n)` and the **private key** is `(d, n)`. The attack works by reversing this process. If an attacker can factor `n` back into `p` and `q`, they can then compute `φ(n)` and subsequently derive the private key `d`.
""")
