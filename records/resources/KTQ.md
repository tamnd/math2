---
records:
    - id: KTQFMY1ZNE
      kind: monograph
      title: Ergodic Theory, Groups, and Geometry
      creators:
        - name: Robert Zimmer
          role: author
        - name: Dave Morris
          role: author
      date: "2008-11-12"
      expressions:
        - key: e1
          kind: edition
          date: "2008-11-12"
          ids:
            doi: 10.1090/cbms/109
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2008-11-12"
              ids:
                isbn:
                    - "9780821809808"
                    - "9780821883365"
                    - "9781470415679"
      relations:
        - kind: part_of
          to: 20XHFD4A67
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/cbms/109
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: KTQYT0AAAB
      kind: course
      title: Introduction to Probability Theory and Stochastic Processes (Tamil)
      creators:
        - name: S Dharmaraja
          role: instructor
      ids:
        course: 049tgcd06:111102518
      expressions:
        - key: e1
          kind: edition
          language: ta
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Delhi
              ids:
                nptel: "111102518"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111102518"
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
