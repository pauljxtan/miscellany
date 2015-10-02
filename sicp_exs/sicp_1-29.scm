; SICP Exercise 1.29
; Integration with Simpson's Rule

(use-modules (ice-9 format))

(define (sum term a next b)
  (if (> a b)
    0
    (+ (term a)
       (sum term (next a) next b))))

(define (simpson f a b n)
  (let ((h (/ (- b a) n)))
    (define (add-2h x) (+ x (* 2 h)))
    (define (term-odd x) (* 4 (f x)))
    (define (term-even x) (* 2 (f x)))
    (* (/ h 3)
       (+ (f a) ; y_0
          (f (+ a (* n h))) ; y_n
          ; odd terms: y_1, y_3, ..., y_{n-3}, y_{n-1}
          (sum term-odd (+ a h) add-2h (- b h))
          ; even terms: y_2, y_4, ..., y_{n-4}, y_{n-2}
          (sum term-even (+ a (* 2 h)) add-2h (- b (* 2 h)))))))

(format #t "f(x)=x^2, a=0, b=1: ~f\n" (simpson (lambda (x) (* x x )) 0 1 1000))
(format #t "f(x)=x^3, a=0, b=1: ~f\n" (simpson (lambda (x) (* x x x)) 0 1 1000))
(format #t "f(x)=x^4, a=0, b=1: ~f\n" (simpson (lambda (x) (* x x x x)) 0 1 1000))
(format #t "f(x)=x^5, a=0, b=1: ~f\n" (simpson (lambda (x) (* x x x x x)) 0 1 1000))
(format #t "f(x)=x^6, a=0, b=1: ~f\n" (simpson (lambda (x) (* x x x x x x)) 0 1 1000))
