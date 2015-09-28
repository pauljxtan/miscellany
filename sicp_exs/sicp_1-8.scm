; SICP Exercise 1.8
; Use Newton's method to approximate cube roots

(use-modules (ice-9 format))

(define (average x y)
  (/ (+ x y) 
     2))

(define (square x)
  (* x x))

(define (cube x)
  (* x x x))

(define (cbrt x)
  (define (good-enough? guess x)
    (< (abs (- (cube guess) 
               x))
       0.000001))
  ; (x/y^2 + 2*y) / 3
  (define (improve guess x)
    (average guess
             (/ (+ (/ x 
                      (square guess)) 
                   (* 2 guess))
                3)))
  (define (cbrt-iter guess x)
    (if (good-enough? guess x)
      guess
      (cbrt-iter (improve guess x) 
                 x)))
  (cbrt-iter 1.0 x))

(format #t "cbrt(8)   = ~f\n" (cbrt 8))
(format #t "cbrt(27)  = ~f\n" (cbrt 27))
(format #t "cbrt(64)  = ~f\n" (cbrt 64))
(format #t "cbrt(125) = ~f\n" (cbrt 125))
(format #t "cbrt(216) = ~f\n" (cbrt 216))
(format #t "cbrt(343) = ~f\n" (cbrt 343))
