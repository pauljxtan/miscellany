; SICP Exercise 1.39
; Approximate tan(x) with continued fraction

(use-modules (ice-9 format))

(define (tan-cf-rec x i k)
  (define (n i) (if (= i 1) x (* x x)))
  (define (d i) (- (* 2 i) 1))
  (if (= i k)
    1
    (/ (n i)
       (- (d i)
          (tan-cf-rec x (+ i 1) k)))))

(define (tan-cf x k)
  (tan-cf-rec x 1 k))

(format #t "tan(0)      = ~f\n" (tan-cf 0 100))
(format #t "tan(pi/4)   = ~f\n" (tan-cf 0.78539816339 100))
(format #t "tan(3*pi/4) = ~f\n" (tan-cf 2.35619449019 100))

