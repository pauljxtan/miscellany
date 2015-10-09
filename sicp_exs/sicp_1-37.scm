; SICP Exercise 1.37
; k-term finite continued fraction

; Doing a recursive version...
;
(use-modules (ice-9 format))

(define (cont-frac-rec n d i k)
  (if (= i k)
    1
    (/ (n i)
       (+ (d i)
          (cont-frac-rec n d (+ i 1) k)))))

(define (cont-frac n d k)
  (cont-frac-rec n d 1 k))

(format #t "(k=2)   1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 2))
(format #t "(k=4)   1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 4))
(format #t "(k=8)   1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 8))
(format #t "(k=16)  1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 16))
(format #t "(k=32)  1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 32))
(format #t "(k=64)  1/phi = ~f\n" (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 64))
