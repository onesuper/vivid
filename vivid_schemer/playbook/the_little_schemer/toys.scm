(begin
    (atom? (quote atom))
    (atom? (quote turkey))
    (atom? (quote 1492))
    (atom? (quote u))
    (atom? (quote *abc$))
    (list? (quote (atom)))
    (list? (quote (atom turkey or)))
    (list? (quote ((atom turkey) or)))
    (sexp? (quote xyz))
    (sexp? (quote (xyz)))
    (list? (quote (((how) are) ((you) (doing so)) far)))
    (how_many_sexp_in_the_list? (quote (((how) are) ((you) (doing so)) far)))
    (how_many_sexp_in_the_list? (quote (how are you doing so far)))
    (list? (quote ()))
    (atom? (quote ()))
    (list? (quote (() () () ())))
    (car (quote (((hotdogs)) (and) (pickle) relish)))
    (car (car (quote (((hotdogs)) (and)))))
    (car (quote ()))
    (car (quote ((a b c) x y z)))
    (car (quote hotdog))
    (car (quote (a b c)))
    (cdr (quote (a b c)))
    (cdr (quote ((a b c) x y z)))
    (cdr (quote (hamburger)))
    (cdr (quote ((x) t r)))
    (cdr (quote hotdogs))
    (cdr (quote ()))
)