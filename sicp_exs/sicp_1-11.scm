; SICP Exercise 1.11
; Compute the given function using both recursive and iterative procedures

(use-modules (ice-9 format))

;==== Recursive version

(define (f-rec n)
  (if (< n 3)
    n
    (+ (f-rec (- n 1))
       (* 2 (f-rec (- n 2))) 
       (* 3 (f-rec (- n 3))))))

;==== Iterative version

(define (f n)
  (f-iter 2 1 0 n))

(define (f-iter a b c count)
  (if (= count 0)
    c
    (f-iter (+ a
               (* 2 b) 
               (* 3 c))
            a
            b
            (- count 1))))

(format #t "==== RECURSIVE\n")
(format #t "f(0) = ~d\n" (f-rec 0))
(format #t "f(1) = ~d\n" (f-rec 1))
(format #t "f(2) = ~d\n" (f-rec 2))
(format #t "f(3) = ~d\n" (f-rec 3))
(format #t "f(4) = ~d\n" (f-rec 4))
(format #t "f(5) = ~d\n" (f-rec 5))
(format #t "f(6) = ~d\n" (f-rec 6))
(format #t "f(7) = ~d\n" (f-rec 7))
(format #t "f(8) = ~d\n" (f-rec 8))
(format #t "f(9) = ~d\n" (f-rec 9))
(format #t "==== ITERATIVE\n")
(format #t "f(0) = ~d\n" (f 0))
(format #t "f(1) = ~d\n" (f 1))
(format #t "f(2) = ~d\n" (f 2))
(format #t "f(3) = ~d\n" (f 3))
(format #t "f(4) = ~d\n" (f 4))
(format #t "f(5) = ~d\n" (f 5))
(format #t "f(6) = ~d\n" (f 6))
(format #t "f(7) = ~d\n" (f 7))
(format #t "f(8) = ~d\n" (f 8))
(format #t "f(9) = ~d\n" (f 9))

