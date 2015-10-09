; SICP Exercise 1.41 & 1.42 & 1.43
; Higher-order procedures / function composition

(use-modules (ice-9 format))

(define (inc x) (+ x 1))
(define (square x) (* x x))

; Exercise 1.41:

(define (double f)
  (lambda (x) (f (f x))))

; Exercise 1.42:

(define (compose f g)
  (lambda (x) (f (g x))))

; (double f) is just (compose f f)
(define (double-alt f)
  (compose f f))

; Exercise 1.43:

(define (repeated-rec f i k)
  (if (= i k)
    f
    (compose f (repeated-rec f (+ i 1) k))))

(define (repeated f k)
  (repeated-rec f 1 k))

(format #t "1+1     = ~d\n" (inc 1))
(format #t "(1+1)+1 = ~d\n" ((double inc) 1))
(newline)
(format #t "2^2     = ~d\n" (square 2))
(format #t "(2^2)^2 = ~d\n" ((double-alt square) 2))
(newline)
(format #t "(6+1)^2 = ~d\n" ((compose square inc) 6)) 
(newline)
(format #t "(5^2)^2 = ~d\n" ((repeated square 2) 5))

