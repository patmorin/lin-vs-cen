The referee had 4 broad comments:

1. The paper's title is a bit ambitious since, as the authors point out, the machinery for relating the linear chromatic number to the centred one was already introduced previously (and this manuscript does not develop on it at all). A more honest title would be something along the lines of "The linear chromatic number of pseudogrids".  
We have chosen to leave the title as is.  In our opinion, the current title doesn't promise much.  The proposed title, on the other hand, suggests that the results apply only to pseudogrids.  Consider, for example, the similar-sounding title "The linear chromatic number of cactus graphs."  
With the current title a reader will still learn, within the first two pages that the improvement comes only by studying the linear chromatic number pseudogrids and decide for themselves whether it's worthwhile reading the rest of the argument.  (These first two pages also have the benefit of catching-up a reader on the current state of the art and the limitations of Kun et al's argument.)

2. There are a few places (e.g. in section 3.6 -- see PDF) where the authors cut a few corners in their proofs; this should be addressed, but I don't think it is anything serious.  

We have gone through the attached PDF carefully and corrected the minor issues pointed out. Some larger changes in response to the referee's comments are discussed below.

3. A lot of the arguments in the middle sections, such as the packing lemma, seem to use the underlying intuition that grids (and by extension pseudogrids) look like the plane with the taxicab metric and the Lebesgue measure. I imagine the authors have already attempted this, but is there really no way to make that intuition rigorous by defining a metric and/or a measure on appropriate sets, and express the lemmas in terms of those? Something like that would make arguments such as the one in Lemma 13 much cleaner. In this direction, have the authors considered the idea of using a grid with every edge subdivided once as the index set for the path partition of the pseudogrid (the subdivision vertices symbolising the edges), with the purpose of making definitions such as the r-boxes more uniform (and of having a symmetric relation, whereby if \mu is in the r-box of \nu, then \nu should be in the r-box of \mu)?  

During the initial writing phase of this result, we tried several such strategies.  The main annoying issue is that mapping the vertices of a subdivided grid onto objects in the pseudogrid sometimes maps a vertex onto a single edge (but not the endpoints of that edge).  In terms of colouring, this means that the subdivision vertex has an empty colour set.  It is possible to define things carefully enough for this to work, but then the reader is constantly having to verify that simple-sounding statements are correct under these careful definitions.

4. In the acknowledgements, the authors mention that it was pointed out to them the problem on a grid (as opposed to pseudogrid) has a simple solution. Assuming the person who pointed that out is happy with it, it might be interesting to include the solution.  

TODO

---

**Referee Comment:** Bottom of Page 2: A tiny bit misleading (since as far as I can tell, the bottleneck for getting conjecture 2 is the grid theorem, not this).  

Top of Page 3: This somewhat addresses the previous comment.

**Response:** We have added further explanation of the limits of this argument here. In particular, even with an Excluded Grid Theorem that matches the currently known lower bound, this would only establish that the centred chromatic number is at most cubic in the linear chromatic number.  Even for planar graphs, the argument can only show that the centred chromatic number is at most quadratic in the linear chromatic number.


**Referee Comment:** I do not understand how this works when removing edges in $P_{v_i}$ -- doesn't $P_{v_i}$ belong to both a row and a column (and thus deleting it leaves us with both fewer rows and columns?)

**Response:** The referee is correct.  The description of deletion has been corrected.  Now we only delete edges of $G$ that correspond to edges of the grid (and then repeatedly remove vertices of degree at most $1$).

**Referee Comment:** $d$ has not been defined. The last part of the proof (where it is shown that a certain value of $d$ would work) should come first -- or at the very least, $d$ should be chosen bigger than some bound given here (and the last part of the proof would show this bound works). This is important, since I am having some trouble keeping track of the dependencies between the variables, so that should be made more transparent.

**Response:** The variable $d$ is defined in the statement of the lemma ("there exists a value $d\in O(r^4\log r)$ such that....").  In the first line of the proof, we use this value of $d$ to apply Lemma 9 to obtain an assignment of colours of objects so that each colour is assigned to at least $d$ objects.  We have expanded the first line of the proof to point this out, so that it is familiar when it is mentioned again at this point in the proof.

**Referee Comment:** From what I can tell, we are saying that if there are enough elements of $\phi^{-1}(\alpha)$ far from the elements of $Q_1$, there will be two such elements far from each other. I agree with this in principle, but where does the actual bound given here come from? The intuition, I presume, is that a set of that size is "maximal" of diameter at most $2r + 1$, but how is that made rigorous? Presumably some argument involving convexity,  and it would be good to see it written.

**Response:** It is much simpler than this.  If more than $\boxplus_{r+1}$ objects of $\phi^{-1}(\alpha)$ are left uncovered by the radius $2r+1$ boxes around the objects in $Y$ then this was also the case when the colour $\alpha$ was considered in the first round.  At that point, we could have chosen any of these uncovered objects $\mu_1$ of colour $\alpha$.  Then $B_{2r+1}(\mu_1)$ contains at most $\boxplus_r$ objects (by definition), so there is still another uncovered object $\mu_2$ of colour $\alpha$.  In this case, we would have put $\mu_1$ and $\mu_2$ into $Q_1$ and round 1 would have succeeded for $\alpha$.
