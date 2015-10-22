; SICP Exercise 2.2
; Representing line segments on a plane

(use-modules (ice-9 format))

;---- Line segments
; Constructor
(define (make-segment start end)
  (cons start end))

; Selectors
(define (start-segment line)
  (car line))
(define (end-segment line)
  (cdr line))
;----
;
;---- Points
; Constructor
(define (make-point x y)
  (cons x y))

; Selectors
(define (x-point point)
  (car point))
(define (y-point point)
  (cdr point))
;----

; Get midpoint of segment
; ((x1+x2)/2, (y1+y2)/2)
(define (midpoint-segment line)
  (make-point (/ (+ (x-point (start-segment line))
                    (x-point (end-segment line)))
                 2)
              (/ (+ (y-point (start-segment line))
                    (y-point (end-segment line)))
                 2)))

; Print point as (x, y)
(define (print-point p)
  (format #t "(~f, ~f)\n" (x-point p) (y-point p)))

; Test procedure
(define (test-midpoint x-start y-start x-end y-end)
  (let ((point-start (make-point x-start y-start))
        (point-end (make-point x-end y-end)))
    (print-point (midpoint-segment (make-segment point-start point-end)))))

(test-midpoint 1.3 5.7 2.4 6.8)
