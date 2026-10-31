---
records:
    - id: Z1YA6SKEV8
      kind: edited-volume
      title: Prediction and Discovery
      creators:
        - name: Joseph Stephen Verducci
          role: editor
        - name: Xiaotong Shen
          role: editor
        - name: John Lafferty
          role: editor
      date: "2007"
      expressions:
        - key: e1
          kind: edition
          date: "2007"
          ids:
            doi: 10.1090/conm/443
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2007"
              ids:
                isbn:
                    - "9780821841952"
                    - "9780821857724"
                    - "9780821881224"
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/443
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: Z1YWDHB4BC
      kind: course-material
      title: 'Lecture 29: Singular value decomposition'
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
                ocw: 18-06-linear-algebra-spring-2010/resources/lecture-29-singular-value-decomposition
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
          native_id: 18-06-linear-algebra-spring-2010/resources/lecture-29-singular-value-decomposition
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
