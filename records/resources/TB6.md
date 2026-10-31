---
records:
    - id: TB6FGSV828
      kind: monograph
      title: 'Interpolation Spaces: An Introduction'
      creators:
        - name: Jöran Bergh
          role: author
        - name: Jörgen Löfström
          role: author
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi: 10.1007/978-3-642-66451-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783642664533"
                    - "9783642664519"
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-66451-9
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: TB6RVAGR3W
      kind: course-material
      title: 'Lecture 16: Projection matrices and least squares'
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          manifestations:
            - key: m1
              kind: page
              publisher: MIT OpenCourseWare
              date: "2010"
              ids:
                ocw: 18-06-linear-algebra-spring-2010/resources/lecture-16-projection-matrices-and-least-squares
      relations:
        - kind: part_of
          to: GE3WH5EF6G/e1
          source: cluster/1
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: ocw
          snapshot: blake3:ab57e74d727dbbb8cc6f30102b1562b267a6d76a54ffa725885e5e4ddfbb57b8
          native_id: 18-06-linear-algebra-spring-2010/resources/lecture-16-projection-matrices-and-least-squares
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
---
