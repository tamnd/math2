---
records:
    - id: 5SHED29H9V
      kind: course
      title: Algebraic Topology
      creators:
        - name: G.K. Srinivasan
          role: instructor
      ids:
        course: 02qyf5152:111101002
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Bombay
              ids:
                nptel: "111101002"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111101002"
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
    - id: 5SHYB7TPS1
      kind: monograph
      title: On Dirichlet's Boundary Value Problem
      creators:
        - name: Christian G. Simader
          role: author
      date: "1972"
      msc:
        - code: 35J35
          from: zbmath_search
        - code: 35J40
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1972"
          ids:
            doi: 10.1007/bfb0058774
            zbl: "0242.35027"
            zbl_id: "3382905"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1972"
              ids:
                isbn:
                    - "9783540059035"
                    - "9783540375890"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0058774
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3382905"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
