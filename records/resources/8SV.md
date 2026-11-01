---
records:
    - id: 8SVDW9DHH3
      kind: monograph
      title: Sequences, Discrepancies and Applications
      creators:
        - name: Michael Drmota
          role: author
        - name: Robert F. Tichy
          role: author
      date: "1997"
      msc:
        - code: 11K06
          from: zbmath_search
        - code: 11-02
          from: zbmath_search
        - code: 11K38
          from: zbmath_search
        - code: 65C10
          from: zbmath_search
        - code: 65D30
          from: zbmath_search
        - code: 11K45
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1997"
          ids:
            doi: 10.1007/bfb0093404
            zbl: "0877.11043"
            zbl_id: "1001300"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1997"
              ids:
                isbn:
                    - "9783540626060"
                    - "9783540683339"
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
          native_id: 10.1007/bfb0093404
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1001300"
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
    - id: 8SVVEVGMNE
      kind: preprint
      title: Algebraically Closed Fields in Equivariant Algebra
      creators:
        - name: Jason Schuchardt
          role: author
        - name: Ben Spitz
          role: author
        - name: Noah Wisdom
          role: author
      date: "2025-05-08"
      msc:
        - code: 55-XX
          from: arxiv
        - code: 13-XX
          from: arxiv
        - code: 19-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.AT
        - system: arxiv
          code: math.AC
        - system: arxiv
          code: math.KT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2025-05-08"
          ids:
            arxiv: "2505.05539"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2505.05539"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2505.05539"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
