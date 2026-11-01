---
records:
    - id: 7RX50B65SB
      kind: problem-set
      title: IMO 1974
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "1974"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1974"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "1974"
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
    - id: 7RXAP2GXXD
      kind: monograph
      title: Difference Spaces and Invariant Linear Forms
      creators:
        - name: Rodney Nillsen
          role: author
      date: "1994"
      msc:
        - code: 43-02
          from: zbmath_search
        - code: 42-02
          from: zbmath_search
        - code: 42B10
          from: zbmath_search
        - code: 43A15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1994"
          ids:
            doi: 10.1007/bfb0073511
            zbl: "0830.43003"
            zbl_id: "706239"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783540583233"
                    - "9783540486527"
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
          native_id: 10.1007/bfb0073511
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "706239"
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
