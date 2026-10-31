---
records:
    - id: Y4CR4N9FBV
      kind: monograph
      title: 'Analyse Harmonique Non-Commutative sur Certains Espaces Homogenes: Etude de Certaines Intégrales Singulières'
      creators:
        - name: Ronald R. Coifman
          role: author
        - name: Guido Weiss
          role: author
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi: 10.1007/bfb0058946
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540057031"
                    - "9783540370765"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0058946
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: Y4CTYDA641
      kind: course
      title: Basic Linear Algebra
      creators:
        - name: I.K.Rana
          role: instructor
      ids:
        course: 02qyf5152:111101115
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Bombay
              ids:
                nptel: "111101115"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111101115"
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
