; SICP Exercise 2.2
; Representing rectangles on a plane

(use-modules (ice-9 format))
 
(define (square x)
  (* x x))

;---- Points: (x, y)
; Constructor
(define (make-point x y)
  (cons x y))

; Selectors
(define (x-point point)
  (car point))
(define (y-point point)
  (cdr point))

; Distance between points
(define (distance-points point1 point2)
  (sqrt(+ (square (- (x-point point1)
                     (x-point point2)))
          (square (- (y-point point1)
                     (y-point point2))))))


; Print point as (x, y)
(define (print-point p)
  (format #t "(~f, ~f)\n" (x-point p) (y-point p)))
;----

;---- Line segments: (start point, end point)
; Constructor
(define (make-segment x-start y-start x-end y-end)
  (cons (make-point x-start y-start) (make-point x-end y-end)))

; Selectors
(define (start-segment line)
  (car line))
(define (end-segment line)
  (cdr line))

; Length of segment
; sqrt((x2-x1)^2 + (y2-y1)^2)
(define (length-segment line)
  (sqrt(+ (square (- (x-point (end-segment line))
                     (x-point (start-segment line))))
          (square (- (y-point (end-segment line))
                     (y-point (start-segment line)))))))
;----

;---- Rectangles: line representation
; ((bottom side, top side), (left side, right side))
; Constructor (parameters are the x and y coordinates of each corner point)
(define (make-rectangle-lines bottom-left-x bottom-left-y
                              bottom-right-x bottom-right-y
                              top-left-x top-left-y
                              top-right-x top-right-y)
  (attach-tag 'lines (cons (cons (make-segment bottom-left-x bottom-left-y
                                               bottom-right-x bottom-right-y)
                                 (make-segment top-left-x top-left-y
                                               top-right-x top-right-y))
                           (cons (make-segment bottom-left-x bottom-left-y
                                               top-left-x top-left-y)
                                 (make-segment bottom-right-x bottom-right-y
                                               top-right-x top-right-y)))))

; Selectors
(define (bottom-line rectangle)
  (car (car (get-contents rectangle))))
(define (top-line rectangle)
  (cdr (car (get-contents rectangle))))
(define (left-line rectangle)
  (car (cdr (get-contents rectangle))))
(define (right-line rectangle)
  (cdr (cdr (get-contents rectangle))))
;---

;---- Rectangles: point representation
; ((bottom left, bottom right), (top left, top right))
; Constructor (parameters are the x and y coordinates of each corner point)
(define (make-rectangle-points bottom-left-x bottom-left-y
                               bottom-right-x bottom-right-y
                               top-left-x top-left-y
                               top-right-x top-right-y)
  (attach-tag 'points (cons (cons (make-point bottom-left-x bottom-left-y)
                                  (make-point bottom-right-x bottom-right-y))
                            (cons (make-point top-left-x top-left-y)
                                  (make-point top-right-x top-right-y)))))

; Selectors
(define (bottom-left-point rectangle)
  (car (car (get-contents rectangle))))
(define (bottom-right-point rectangle)
  (cdr (car (get-contents rectangle))))
(define (top-left-point rectangle)
  (car (cdr (get-contents rectangle))))
(define (top-right-point rectangle)
  (cdr (cdr (get-contents rectangle))))
;----

(define (attach-tag get-tag contents)
  (cons get-tag contents))

(define (get-tag pair)
  (car pair))

(define (get-contents pair)
  (cdr pair))

(define (line-repr? pair)
  (eq? (get-tag pair) 'lines))
(define (point-repr? pair)
  (eq? (get-tag pair) 'points))

; Length of rectangle (bottom edge)
(define (length-rectangle rectangle)
  (cond ((line-repr? rectangle)
         (length-segment (bottom-line rectangle)))
        ((point-repr? rectangle)
         (distance-points (bottom-left-point rectangle) (bottom-right-point rectangle)))))

; Width of rectangle (left edge)
(define (width-rectangle rectangle)
  (cond ((line-repr? rectangle)
         (length-segment (left-line rectangle)))
        ((point-repr? rectangle)
         (distance-points (bottom-left-point rectangle) (top-left-point rectangle)))))

; Perimeter of rectangle (2*length + 2*width)
(define (perimeter-rectangle rectangle)
  (+ (* 2 (length-rectangle rectangle))
     (* 2 (width-rectangle  rectangle))))

; Area of rectangle (length * width)
(define (area-rectangle rectangle)
  (* (length-rectangle rectangle)
     (width-rectangle  rectangle)))
;----

; Test procedure
(define (test-perimeter-area bottom-left-x bottom-left-y
                             bottom-right-x bottom-right-y
                             top-left-x top-left-y
                             top-right-x top-right-y)
  (let ((rect-lines (make-rectangle-lines bottom-left-x bottom-left-y
                                          bottom-right-x bottom-right-y
                                          top-left-x top-left-y
                                          top-right-x top-right-y))
        (rect-points (make-rectangle-points bottom-left-x bottom-left-y
                                            bottom-right-x bottom-right-y
                                            top-left-x top-left-y
                                            top-right-x top-right-y)))

    (format #t "LINE REPRESENTATION:  Perimeter=~f, Area=~f\n"
            (perimeter-rectangle rect-lines) (area-rectangle rect-lines))
    (format #t "POINT REPRESENTATION: Perimeter=~f, Area=~f\n"
            (perimeter-rectangle rect-points) (area-rectangle rect-points))
))

(test-perimeter-area 0 0
                     0 2
                     3 0
                     3 2)
