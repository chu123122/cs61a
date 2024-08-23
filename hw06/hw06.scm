(define (square n) (* n n))

(define (pow base exp)
       (cond    ((= exp 0) 1)
                ((even? exp) (square (pow base (/ exp 2))))
                (else (* base (pow base (- exp 1))))
       )
)
; (define (pow base exp)
;   (cond ((= exp 0) 1)
;         ((even? exp) (square (pow base (/ exp 2))))
;         (else (* base (pow base (- exp 1)))))
; )

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
        (car (cdr s))
)

(define (caddr s) 
        (car  (cddr s))
)

(define (ascending? s) 
        (if (or (null? s) (null? (cdr s)))
                #t
                (if (<=(car s) (car(cdr s)))
                        (ascending? (cdr s))
                        #f
                )
        )
)

(define (my-filter pred s) 
        (if (null? s)
                '()
                (if (pred (car s))
                        (cons   (car s)
                                (my-filter pred (cdr s))
                        )
                        (my-filter pred (cdr s))
                )
        )
)

(define (no-repeats s) 
        (define (helper number s)
                (if (null? s)
                        #t
                        (if (not (= number (car s)))
                                (helper number (cdr s))        
                                #f
                        )
                )
        )
        (my-filter (lambda (number) (helper number s)) s )
)
; (define (no-repeats s)
;   (if (null? s) s
;     (cons (car s)
;       (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
; )

; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
  ______________________________________________)

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                     (larger-values first rest))
             (define with-first
                     ______________________________________________)
             (define without-first
                     ______________________________________________)
             (if ______________________________________________
                 with-first
                 without-first))))
