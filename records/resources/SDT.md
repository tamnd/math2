---
records:
    - id: SDTCZHR9FQ
      kind: course
      title: Complex Analysis
      creators:
        - name: Pranav Haridas
          role: instructor
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: Kerala School of Mathematics
              ids:
                nptel: "111106141"
      scope:
        value: in
        rule: S6
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106141"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: SDTYB6W40M
      kind: monograph
      title: Adaptive Moving Mesh Methods
      creators:
        - name: Weizhang Huang
          role: author
        - name: Robert D. Russell
          role: author
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
          ids:
            doi: 10.1007/978-1-4419-7916-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781441979155"
                    - "9781441979162"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-7916-2
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
