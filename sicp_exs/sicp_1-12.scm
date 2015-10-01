; SICP Exercise 1.12
; Recursively compute the elements Pascal's triangle

(use-modules (ice-9 format))

; Computes the value at a given position on a given row
; (Note that the row number equals the number of elements in that row)
; (Indices start at zero)
(define (pascal-elem row pos)
  ; The left-most and right-most elements is always 1
  (if (or (= pos 0) (= pos row))
    1
    ; All other elements are the sum of the two elements above it
    (+ (pascal-elem (- row 1) (- pos 1))
       (pascal-elem (- row 1) pos ))))

(format #t "     ~d          \n" (pascal-elem 0 0))
(format #t "    ~d ~d        \n" (pascal-elem 1 0) (pascal-elem 1 1))
(format #t "   ~d ~d ~d      \n" (pascal-elem 2 0) (pascal-elem 2 1)
                              (pascal-elem 2 2))
(format #t "  ~d ~d ~d ~d    \n" (pascal-elem 3 0) (pascal-elem 3 1)
                              (pascal-elem 3 2) (pascal-elem 3 3))
(format #t " ~d ~d ~d ~d ~d  \n" (pascal-elem 4 0) (pascal-elem 4 1)
                              (pascal-elem 4 2) (pascal-elem 4 3)
                              (pascal-elem 4 4))
