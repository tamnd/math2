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
      msc:
        - code: 43-02
          from: zbmath_search
        - code: 43A15
          from: zbmath_search
        - code: 43A22
          from: zbmath_search
        - code: 22C05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1971"
          ids:
            doi: 10.1007/bfb0058946
            zbl: "0224.43006"
            zbl_id: "3355709"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540057031"
                    - "9783540370765"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0058946
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3355709"
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
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
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
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
