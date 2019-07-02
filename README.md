<h1 align='center'>
  Bisection.
</h1>

- ``Python -v 3.6``

#### How to use Bisection

- ``fork`` and ``clone`` repo.
- create a virtual environment use ``virtualenv -p python3 envname``.
- Inside the ``virtualenv`` pip install ``pytest``.
- To run test cd into ``bisection`` and type ``pytest``.


>The Bisection Method is a successive approximation method that narrows down an interval that contains a root of the function f(x).

> The Bisection Method is given an initial interval [a..b] that contains a root
(We can use the property sign of f(a) ≠ sign of f(b) to find such an initial interval)

> The Bisection Method will cut the interval into 2 halves and check which half interval contains a root of the function
The Bisection Method will keep cut the interval in halves until the resulting interval is extremely small
The root is then approximately equal to any value in the final (very small) interval.

Thes expample uses the bisection method to guess a number from 0 to the set ``range``.

<img width="509" alt="Screen Shot 2019-07-02 at 13 00 38" src="https://user-images.githubusercontent.com/37377831/60511309-87aafb80-9cc9-11e9-88c9-be9e94c8c8eb.png">

> Note that the default range is 10

<img width="1280" alt="Screen Shot 2019-07-02 at 13 01 07" src="https://user-images.githubusercontent.com/37377831/60511381-b628d680-9cc9-11e9-8547-cb53a870891e.png">

- The algorithm works really well but it can be imporved to make the guess in under 6 guesses. ``(this is the next todo)``