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

(define (cbrt x delta init-guess)
  
  (define (good-enough? guess)
    (< (abs (- (cube guess) 
               x))
       delta))
  
  ; (x/y^2 + 2*y) / 3
  (define (improve guess)
    (average guess
             (/ (+ (/ x 
                      (square guess)) 
                   (* 2 guess))
                3)))
  
  (define (cbrt-iter guess)
    (if (good-enough? guess)
      guess
      (cbrt-iter (improve guess))))

  (cbrt-iter init-guess)
)

(format #t "cbrt(8)   = ~f\n" (cbrt 8 0.000001 1.0))
(format #t "cbrt(27)  = ~f\n" (cbrt 27 0.000001 1.0))
(format #t "cbrt(64)  = ~f\n" (cbrt 64 0.000001 1.0))
(format #t "cbrt(125) = ~f\n" (cbrt 125 0.000001 1.0))
(format #t "cbrt(216) = ~f\n" (cbrt 216 0.000001 1.0))
(format #t "cbrt(343) = ~f\n" (cbrt 343 0.000001 1.0))
