---
records:
    - id: RHP5ZNXKPX
      kind: course
      title: Complex Analysis
      creators:
        - name: P. A. S. Sree Krishna
          role: instructor
      ids:
        course: 0022nd079:111103070
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Guwahati
              ids:
                nptel: "111103070"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111103070"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: RHPXN7XV60
      kind: monograph
      title: Conformal Dimension
      creators:
        - name: John Mackay
          role: author
        - name: Jeremy Tyson
          role: author
      date: "2010-06-22"
      expressions:
        - key: e1
          kind: edition
          date: "2010-06-22"
          ids:
            doi: 10.1090/ulect/054
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2010-06-22"
              ids:
                isbn:
                    - "9781470416492"
                    - "9780821883105"
                    - "9780821852293"
      relations:
        - kind: part_of
          to: CMK1G7XE8B
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/ulect/054
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
